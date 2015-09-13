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
  buildToggle = (navID) ->
    debounceFn = $mdUtil.debounce((->
      $mdSidenav(navID).toggle().then ->
    ), 200)
    debounceFn
  $scope.toggleLeft = buildToggle('left')
  $scope.toggleRight = buildToggle('right')
  # background gradient
  $scope.menuBackground = (index) ->
    menuLen = 10
    hBase = 210
    hDelta = 0
    sBase = 60
    sDelta = 30
    lBase = 50
    lDelta = 30

    h = hBase + (index / menuLen) * hDelta
    s = sBase + (index / menuLen) * sDelta
    l = lBase + (index / menuLen) * lDelta

    style = {'background-color': 'hsl(' + h + ',' + s + '%,' + l + '%)'}
    style

).controller('LeftCtrl', ($scope, $timeout, $mdSidenav, $log, $location) ->
  $scope.jump = (url) ->
    $location.path(url)

  $scope.menus = [
    {type: 'action', name: 'Search', ngClick: $scope.toggleRight, param: ''},
#    {type: 'divider'},
    {type: 'action', name: 'Home', ngClick: $scope.jump, param: '/'}
    {type: 'action', name: 'Blog', ngClick: $scope.jump, param: '/blog'}
  ]

  # background gradient
  $scope.menuBackground = (index) ->
    menuLen = $scope.menus.length + 1
    if index == -1
      index = menuLen
    hBase = 200
    hDelta = 0
    sBase = 60
    sDelta = 30
    lBase = 50
    lDelta = 30

    h = hBase + (index/menuLen) * hDelta
    s = sBase + (index/menuLen) * sDelta
    l = lBase + (index/menuLen) * lDelta

    style = {'background-color': 'hsl('+h+','+s+'%,'+l+'%)'}
    style

  $scope.close = ->
    $mdSidenav('left').close().then ->
).controller 'RightCtrl', ($scope, $timeout, $mdSidenav, $log) ->
  $scope.close = ->
    $mdSidenav('right').close().then ->
      $log.debug 'close RIGHT is done'



