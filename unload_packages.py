import sys

DEFAULT_RELOAD_PACKAGES = ["maya_helper"]

def unload_packages(packages):
    if not packages:
        packages = DEFAULT_RELOAD_PACKAGES
    else:
        packages.extend(DEFAULT_RELOAD_PACKAGES)

    # construct reload list
    reloadList = []
    for i in sys.modules.keys():
        for package in packages:
            if i.startswith(package) and "unload_packages" not in i:
                reloadList.append(i)

    print(reloadList)

    # unload everything
    for i in reloadList:
        try:
            if sys.modules[i] is not None:
                print(sys.modules[i])
                del(sys.modules[i])
                print("Unloaded: %s" % i)
        except:
            print("Failed to unload: %s" % i)