angular.module "angular"
  .run ($log, $rootScope) ->
    $log.debug 'runBlock end'
#    $rootScope.$on("$stateChangeError", console.log.bind(console));

