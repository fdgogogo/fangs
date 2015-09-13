angular.module "angular"
.controller "BlogPostController", (Restangular, $routeParams) ->
  vm = this
  vm.post = Restangular.one(
    'blog_post',
    $routeParams['postSlug']
  ).get().$object
  vm.log = ->
    console.log(vm.post)
  return vm

