angular.module "angular"
.controller "BlogPostController", (Restangular, $stateParams) ->
  vm = this
  console.log($stateParams)
  vm.post = Restangular.one(
    'blog_post',
    $stateParams['postSlug']
  ).get().$object
  return vm

