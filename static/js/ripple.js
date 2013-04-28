Handlebars.registerHelper('friendPhoto', function(friend) {
  var size = 78 * Math.pow(2, friend['weight']);
  return new Handlebars.SafeString('<img src="https://graph.facebook.com/'+friend['uid']+'/picture?width='+size+'&height='+size+'" width="'+size+'" height="'+size+'">');
});
Handlebars.registerHelper('friendPhotoSize', function(friend) {
  return 78 * Math.pow(2, friend['weight']);
});

$(document).ready(function() {
  var fbUser, uid, accessToken, friends, pages, cachedData = {}, cachedArtists = {}, cachedSongs = {};
  $(window).bind('fbAsyncInit', function() {
    FB.getLoginStatus(function(response) {
      if (response.status === 'connected') {
        // the user is logged in and has authenticated your
        // app, and response.authResponse supplies
        // the user's ID, a valid access token, a signed
        // request, and the time the access token 
        // and signed request each expire
        accessToken = response.authResponse.accessToken;
        // goToServer(uid, accessToken);
        refreshCurrentUser();
      } else if (response.status === 'not_authorized') {
        // the user is logged in to Facebook, 
        // but has not authenticated your app
      } else {
        // the user isn't logged in to Facebook.
      }
     });
    Path.listen();
  });
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
  });
  function goToServer(url, responseCb) {
    if (cachedData[url]) {
      console.log('cache hit!');
      if (responseCb) responseCb(cachedData[url]);
    } else {
      FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          accessToken = response.authResponse.accessToken;
          $.post(url, { fbid: response.authResponse.userID, token: accessToken }, function(response) {
            cachedData[url] = response;
            if (responseCb) responseCb(response);
          });
        } else if (response.status === 'not_authorized') {
          // the user is logged in to Facebook, 
          // but has not authenticated your app
        } else {
          // the user isn't logged in to Facebook.
        }
      });
    }
  }
  function refreshCurrentUser(successCb) {
    FB.api('/me', function(response) {
      fbUser = response;
      console.log('Good to see you, ' + response['name'] + '.');
      updateUserNavbar();
      if (successCb) successCb();
    });
  }
  function updateUserNavbar() {
    console.log(fbUser);
    if (fbUser) {
      $('.nav-auth li').show();
      $('.nav-auth .login').hide();
      $('.nav-auth .me a')
        .attr('href', '#/user/'+fbUser['id'])
        .text(fbUser['name']);
      $('.nav-auth .me-img img').attr('src', 'https://graph.facebook.com/'+fbUser['id']+'/picture');
    } else {
      $('.nav-auth li').hide();
      $('.nav-auth .login').show();
    }
  }

  $('.login a').click(function() {
    FB.login(function(response) {
      if (response.authResponse) {
        console.log('Welcome!  Fetching your information.... ');
        refreshCurrentUser(function() {
          window.location.hash = '#/user/'+fbUser['id'];
        });
      } else {
        console.log('User cancelled login or did not fully authorize.');
      }
    }, {scope: 'email,user_actions.music,user_events,user_interests,user_hometown,user_location,user_likes,user_videos,user_interests,user_actions.video,friends_about_me,friends_actions.music,friends_likes,friends_location,friends_hometown,friends_status'});
  });

  $('.logout a').click(function() {
    FB.logout(function(response) {
      fbUser = undefined;
      updateUserNavbar();
    });
  });

  function notFound() {
    console.error('page not found!');
  }
  function ensureLogin() {
    if ( ! fbUser) {
      window.location.hash = '';
    }
  }

  var theContent = $('#the-content');
  var userTpl = Handlebars.compile($('#user-template').html());
  var friendTpl = Handlebars.compile($('#friend-template').html());

  Path
    .map('#/user/:user_id')
    .to(function() {
      if (fbUser && fbUser['id'] == this.params['user_id']) {
        renderDiscoverPage(fbUser);
      } else {
        FB.api('/'+this.params['user_id'], function(response) {
          fbUser = response;
          //@todo check validity of response
          renderDiscoverPage(response);
        });
      }
    });

  function renderDiscoverPage(user) {
    theContent.html(userTpl({
      activeDiscover: true,
      user: user
    }));
    goToServer('ajax/login', function(response) {
      friends = response.friends;
      pages = response.pages;
      response.user = user;
      $('.friends').html(friendTpl(response)).masonry({
        // options
        itemSelector : '.item'
      });
    });
  }

  // function findFriendById(id, foundCb) {
  //   goToServer(function(response) {
  //     for (friend in response.friends) {
  //       if (friend.uid == id) {
  //         foundCb(friend);
  //         break;
  //       }
  //     }
  //   });
  // }
    $.widget( "custom.catcomplete", $.ui.autocomplete, {
    _renderMenu: function( ul, items ) {
      var that = this,
        currentCategory = "";
      $.each( items, function( index, item ) {
        if ( item.category != currentCategory ) {
          ul.append( "<li class='ui-autocomplete-category'>" + item.category + "</li>" );
          currentCategory = item.category;
        }
        that._renderItemData( ul, item );
      });
    }
  });

    var to_be_searched = []

    $("#search").catcomplete({
      source: function(req, add){
        if (!friends && !pages) {
          return;
        }
        var suggestions = [];
        $.each(friends, function(i, user){
          if (user.name.toLowerCase().indexOf(req.term.toLowerCase()) !== -1){
          suggestions.push({'value':user.name, 'id': user.uid, 'category' : 'Friends'});}
        });
        $.each(pages, function(i, page){
          if (page.name.toLowerCase().indexOf(req.term.toLowerCase()) !== -1){
          suggestions.push({'value':page.name, 'id': page.id, 'category' : 'Artists'});}
        });
        add(suggestions);
      },
      select: function(e, ui){
        // var friend = ui.item.value,
        // span = $('<span class="autocomplete-added">').text(friend),
        // a = $("<a>").addClass("remove").attr({
        //   href: "javascript:",
        //   title: "Remove " + friend
        // }).text("x ").appendTo(span);
        // span.insertBefore("#search");
        // to_be_searched.push(ui.item);
        // console.log(to_be_searched);
        window.location.hash = '#/user/'+fbUser['id']+'/friend/'+ui.item.id;
      },
      change: function(){
        $("#search").val("").css("top",2);
      },
      search: function(){
        $.post('ajax/search', to_be_searched, function(search_results){
          console.log(search_results);
        });

      }
    });

  //add click handler to friends div
          
  //add live handler for clicks on remove links
  $(document).on("click", ".remove", function(){
    $(this).parent().remove();
    if($("#friends span").length === 0) {
      $("#to").css("top", 0);
    }       
  });


  function getFriendById(id) {
    for (var i = 0; i < friends.length; i++) {
      if (friends[i].uid == id) {
        console.log('got', friends[i]);
        return friends[i];
      }
    }
  }
  function renderComparePage(user, friend_id) {
    theContent.html(userTpl({
      activeDiscover: true,
      activeFriend: true,
      user: user
    }));
    goToServer('ajax/login', function(response) {
      friends = response.friends;
      pages = response.pages;
      response.user = user;
      theContent.html(userTpl({
        activeDiscover: true,
        activeFriend: true,
        user: user,
        friend: getFriendById(friend_id)
      }));
    });
  }
  Path
    .map('#/user/:user_id/and/:friend_id')
    .to(function() {
      if (fbUser && fbUser['id'] == this.params['user_id']) {
        renderComparePage(fbUser, this.params['friend_id']);
      } else {
        var _this = this;
        FB.api('/'+this.params['user_id'], function(response) {
          fbUser = response;
          //@todo check validity of response
          renderComparePage(fbUser, _this.params['friend_id']);
        });
      }
    });

  function renderArtistPage(artist) {
      theContent.html(userTpl({
        activeArtist: true,
        artist: artist
      }));
      $.post('ajax/artist_events', { name: artist.name }, function(events) {
        for (var i = 0; i < events.length; i++) {
          events[i].image = events[i].venue.image[2]['#text'];
        }
        console.log('got events', events);
        theContent.html(userTpl({
          activeArtist: true,
          artist: artist,
          eventsLoaded: true,
          events: events
        }));
        // $.post('ajax/artist_songs', { name: artist.name }, function(songs) {
        //   console.log('got songs', songs);
        // });
      });
  }
  Path
    .map('#/artist/:artist_id')
    .to(function() {
      var artist_id = this.params['artist_id'];
      console.log('getting ', artist_id);
      theContent.html(userTpl({
        activeArtist: true
      }));
      if (cachedArtists[artist_id]) {
        renderArtistPage(cachedArtists[artist_id]);
      } else {
        FB.api('/'+artist_id, function(response) {
          console.log(response);
          cachedArtists[artist_id] = response;
          //@todo check validity of response
          renderArtistPage(response);
        });
      }
    });

  Path.map('#/').to(function() {
    console.log('home page');
  });

  Path.rescue(notFound);
  Path.root('#/');
});