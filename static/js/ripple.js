$(document).ready(function() {
  var fbUser;
  $(window).bind('fbAsyncInit', function() {
    FB.getLoginStatus(function(response) {
      if (response.status === 'connected') {
        // the user is logged in and has authenticated your
        // app, and response.authResponse supplies
        // the user's ID, a valid access token, a signed
        // request, and the time the access token 
        // and signed request each expire
        var uid = response.authResponse.userID;
        var accessToken = response.authResponse.accessToken;
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

  Path.map('#/user/:user_id').to(function() {
    console.log('looking at ' + this.params['user_id']);
    var user;
    if (fbUser && fbUser['id'] == this.params['user_id']) {
      user = fbUser;
      theContent.html(userTpl(fbUser));
    } else {
      FB.api('/'+this.params['user_id'], function(response) {
        theContent.html(userTpl(response));
      });
    }
  });

  Path.map('#/').to(function() {
    console.log('home page');
  });

  Path.rescue(notFound);
  Path.root('#/');
});