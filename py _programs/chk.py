import pip

installed_packages = pip.get_installed_distributions()
print installed_packages

installed_packages_list = sorted(["%s" % (i.key)
     for i in installed_packages])

if 'pyyaml' in installed_packages_list:
  print True
else:
  print False

