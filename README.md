## Fedora repos for RHEL 8

**This is not the proper way to install things in RHEL 8. **

**But if you did not find a package you want in the EPEL repository, or elsewhere - high chances are that you can find it in Fedora 28 repositories, which are a more or less "compatible" to CentOS/RHEL 8. **

**Remember, the proper way to get a missing package is to rebuild it! This is only a neat workaround when you don't want or cannot build a package**.

### Synopsys

    sudo dnf -y install https://extras.getpagespeed.com/release-el8-latest.rpm
    sudo dnf install fed2el-release
    dnfplus install filezilla

The `fed2el-release` package contains `dnf` repository configurations for Fedora 28.

By running `dnfplus`, you simply enable the Fedora 28 repositories in addition to others - it's merely a shortcut to `--enablerepo ...`.

