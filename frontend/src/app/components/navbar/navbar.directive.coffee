angular.module "angular"
.directive 'acmeNavbar': -> (
  directive =
    restrict: 'E'
    templateUrl: 'app/components/navbar/navbar.html'
    transclude: true
    scope:
      creationDate: '='
    controller: 'AppCtrl'
    controllerAs: 'vm'
    bindToController: true
)
angular.module "angular"
.controller('AppCtrl', ($scope, $timeout, $mdSidenav, $mdUtil, $log) ->
  buildToggler = (navID) ->
    debounceFn = $mdUtil.debounce((->
      $mdSidenav(navID).toggle().then ->
    ), 200)
    debounceFn
  $scope.toggleLeft = buildToggler('left')
  $scope.toggleRight = buildToggler('right')

).controller('LeftCtrl', ($scope, $timeout, $mdSidenav, $log, $location) ->
  $scope.jump = (url) ->
    $location.path(url)
  $scope.menus = [
    {'name': 'Search', ngClick: $scope.toggleRight},
    {'name': 'Home', ngClick: $scope.jump, params: '/'},
    {'name': 'Blog', ngClick: $scope.jump, params: '/blog'}
  ]
  $scope.close = ->
    $mdSidenav('left').close().then ->
).controller 'RightCtrl', ($scope, $timeout, $mdSidenav, $log) ->
  $scope.close = ->
    $mdSidenav('right').close().then ->
      $log.debug 'close RIGHT is done'



