angular.module "angular"
  .run ($log, $rootScope) ->
    $log.debug 'runBlock end'
    $rootScope.$on '$stateChangeError', (event, unfoundState, fromState, fromParams) ->
      console.log event

# ---
