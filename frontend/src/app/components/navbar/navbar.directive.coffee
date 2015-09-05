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

  ###*
  # Build handler to open/close a SideNav; when animation finishes
  # report completion in console
  ###
  buildToggler = (navID) ->
    debounceFn = $mdUtil.debounce((->
      $mdSidenav(navID).toggle().then ->
        $log.debug 'toggle ' + navID + ' is done'
        return
      return
    ), 200)
    debounceFn

  $scope.toggleLeft = buildToggler('left')
  $scope.toggleRight = buildToggler('right')
  return
).controller('LeftCtrl', ($scope, $timeout, $mdSidenav, $log) ->
  $scope.close = ->
    $mdSidenav('left').close().then ->
      $log.debug 'close LEFT is done'
      return
    return

  return
).controller 'RightCtrl', ($scope, $timeout, $mdSidenav, $log) ->
  $scope.close = ->
    $mdSidenav('right').close().then ->
      $log.debug 'close RIGHT is done'
      return
    return

  return



