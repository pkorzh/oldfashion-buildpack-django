import pkg_resources

class Buildpack():
	def detect(self, files):
		return 'manage.py' in files

	def get_build_context_path(self, files):
		return pkg_resources.resource_filename(__name__, "build-context")