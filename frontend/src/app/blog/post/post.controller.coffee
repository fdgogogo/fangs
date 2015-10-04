angular.module "angular"
.controller "BlogPostController", (Restangular, $stateParams) ->
  vm = this
  vm.post = Restangular.one(
    'blog_post',
    $stateParams['slug']
  ).get().$object
  vm.log = ->
    console.log(vm.post)
  return vm

