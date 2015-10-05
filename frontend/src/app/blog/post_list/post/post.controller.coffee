angular.module "angular"
.controller "BlogPostController", (Restangular, $stateParams, $sce) ->
  vm = this
  request = Restangular
  .one(
    'blog_post',
    $stateParams['postSlug']
  )
  .get()
  .then (post) ->
    vm.post = post
  vm.post = null
  return vm
