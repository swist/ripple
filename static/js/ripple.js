window.App = Ember.Application.createWithMixins({
  LOG_TRANSITIONS: true
});

App.User = Ember.Object.extend({
  firstName: null,
  lastName: null,

  fullName: function() {
    return this.get('firstName') +
           " " + this.get('lastName');
  }.property('firstName', 'lastName')
});

App.Store = DS.Store.extend({
  revision: 12,
  adapter: 'DS.FixtureAdapter'
});

App.User = DS.Model.extend({
  firstName: DS.attr('string'),
  lastName: DS.attr('string'),
  location: DS.attr('string')
});

App.User.FIXTURES = [{
  id: 1, firstName: 'Jian Yuan', lastName: 'Lee'
}, {
  id: 2, firstName: 'Jian Yuan 2', lastName: 'Lee'
}];

App.Person = Ember.Object.extend({
  loggedIn: false,
  fbId: null,
  firstName: null,
  lastName: null,
  fullName: function() {
    return this.get('firstName') +
           " " + this.get('lastName');
  }.property('firstName', 'lastName'),
  displayPicture: function() {
    return 'https://graph.facebook.com/'+this.get('fbId')+'/picture';
  }
});

App.ActiveUser = App.Person.create();

App.Router.map(function() {
  this.route('me');
});

App.ApplicationController = Ember.Controller.extend({
  loginFacebook: function() {
    var self = this;
    FB.login(function(response) {
      if (response.authResponse) {
        console.log('User logged in');
        FB.api('/me', function(response) {
          console.log(response);
          App.ActiveUser.set('fbId', response['id']);
          App.ActiveUser.set('firstName', response['first_name']);
          App.ActiveUser.set('lastName', response['last_name']);
          App.ActiveUser.set('location', response['location']['name']);
          App.ActiveUser.set('loggedIn', true);
          self.transitionToRoute('me');
        });
      } else {
        console.log('User cancelled login');
      }
    }, {
      scope: 'email,user_actions.music,user_events,user_interests,user_hometown,user_location,user_likes,user_videos,user_interests,user_actions.video,friends_about_me,friends_actions.music,friends_likes,friends_location,friends_hometown,friends_status'
    });
  }
});

App.IndexRoute = Ember.Route.extend({
  model: function() {
    return ['red', 'yellow', 'blue'];
  }
});