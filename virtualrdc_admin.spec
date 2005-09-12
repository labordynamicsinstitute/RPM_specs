Summary: Tools to configure a VirtualRDC 
Name: virtualrdc_admin 
Version: 1.0.4
Release: 3
Copyright: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: virtualrdc_admin-%{version}.tgz
BuildArch: noarch
Requires: perl, mysql-client


%description
* Provides tools to create user accounts, reset passwords
* Provides tools to create groups

%prep 
set
tar xvzf %{SOURCE0}

%build

%install

export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}/${RPM_PACKAGE_VERSION}/scripts
rm -rf $RPM_BUILD_ROOT/
install -d -m 755 $RPM_BUILD_ROOT/usr/local/sbin
install -m 755    $MYBUILD/vrdc.addusers $RPM_BUILD_ROOT/usr/local/sbin/vrdc.addusers
install -m 755    $MYBUILD/vrdc.resetpass $RPM_BUILD_ROOT/usr/local/sbin/vrdc.resetpass
install -m 755    $MYBUILD/vrdc.creategroups $RPM_BUILD_ROOT/usr/local/sbin/vrdc.creategroups
install -d -m 755 $RPM_BUILD_ROOT/usr/local/bin
install -m 755    $MYBUILD/convert_phonetics.pl $RPM_BUILD_ROOT/usr/local/bin/convert_phonetics.pl

%clean
rm -rf $RPM_BUILD_ROOT/*


%files
%defattr(-,root,root) 
/usr/local/bin/convert_phonetics.pl
/usr/local/sbin/vrdc.resetpass
/usr/local/sbin/vrdc.addusers
/usr/local/sbin/vrdc.creategroups


%changelog
* Mon Feb 21 2005 vilhuber
  - fixes email address domain
* Sat Feb 19 2005 vilhuber
  - first version
