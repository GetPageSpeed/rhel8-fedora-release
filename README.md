## Fedora repos for RHEL 8

**This is not the proper way to install things in RHEL 8. **

**But due to lack of EPEL repository for RHEL 8 now, this is lesser evil in comparison to compiling everything you need or rebuilding every single dependency’s RPM. **

### Synopsys

    sudo dnf -y install https://extras.getpagespeed.com/release-el8-latest.rpm
    sudo dnf install fedora-release
    dnfplus install filezilla