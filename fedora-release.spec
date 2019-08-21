# Fedora 28 RPM Repository configuration files and GPG key
 
Name:           fedora-release
Version:        %{rhel}
Release:        3%{?dist}.gps
Summary:        Fedora packages repository configuration for CentOS/RedHat %{version}.
Group:          System Environment/Base
License:        BSD
URL:            https://www.getpagespeed.com/work/50k-packages-for-rhel-8-centos-8-even-before-epel-is-up
Source0:        fedora.repo
Source1:        fedora-russian.repo
Source2:        fedora-rpmfusion.repo

Source10:       RPM-GPG-KEY-fedora-28-aarch64  
Source11:       RPM-GPG-KEY-fedora-28-i386   
Source12:       RPM-GPG-KEY-fedora-28-ppc64le  
Source13:       RPM-GPG-KEY-fedora-28-s390x

Source20:       RPM-GPG-KEY-russianfedora-free-fedora
Source21:       RPM-GPG-KEY-russianfedora-nonfree-fedora

Source30:       RPM-GPG-KEY-rpmfusion-free-fedora-28     
Source31:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-28-primary  
Source32:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-30          
Source33:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-rawhide
Source34:       RPM-GPG-KEY-rpmfusion-nonfree-fedora     
Source35:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-29          
Source36:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-30-primary
Source37:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-28  
Source38:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-29-primary  
Source39:       RPM-GPG-KEY-rpmfusion-nonfree-fedora-latest

Source100:      dnfplus.sh

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
This package contains Fedora 28 repositories
GPG key as well as configuration for dnf.

After the package installation you will be able to install Fedora
packages to your RHEL/CentOS 8.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%{__install} -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%{__install} -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%{__install} -m 644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%{__install} -m 644 -p %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%{__install} -m 644 -p %{SOURCE30} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE31} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE32} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE33} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE34} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE35} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE36} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE37} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE38} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
%{__install} -m 644 -p %{SOURCE39} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%{__install} -Dp -m0755 %{SOURCE100} $RPM_BUILD_ROOT%{_bindir}/dnfplus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
%{_bindir}/dnfplus

%changelog
* Wed Jun 26 2019 Danila Vershinin <info@getpagespeed.com> 8-2
- alias dnfplus command with sudo so it can be run directly
