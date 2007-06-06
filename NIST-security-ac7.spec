Summary:  Implements AC-07 (NIST 800-53)
Name: NIST-security-ac7
Version: 1.0.0
Release: 1
License: GPL
Vendor: Mohammed Chaudhry
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Group: System/Security
Source0: pam_tally_reset-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
%define filename    %{name}.sh

%description
This implements tools to aid in managing  AC-07 Account Management (NIST 800-53): 
"The information system enforces a limit of [Assignment: organization-defined number] consecutive invalid access attempts by a user during a [Assignment: organization-defined time period] time period. The information system automatically [Selection: locks the account/node for an [Assignment: organization-defined time period], delays next login prompt according to [Assignment: organization-defined delay algorithm.]] when the maximum number of unsuccessful attempts is exceeded." The actual control is implemented through pam_tally, this package implements a cronjob that resets the locks every 15 minutes.

%prep
%setup -n pam_tally_reset-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 700  %buildroot/var/log/pam_tally_reset
install -d -m 755  %buildroot/usr/sbin
install -d -m 700  %buildroot/etc/cron.d
install cronjob %buildroot/etc/cron.d/pam_tally_reset
install pam_tally_reset  %buildroot/usr/sbin/pam_tally_reset

%clean
#rm -rf $RPM_BUILD_ROOT


%files
%defattr(700,root,root,-)
/var/log/pam_tally_reset
/etc/cron.d/pam_tally_reset
/usr/sbin/pam_tally_reset


%changelog
* Wed Jun  6 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1.0.0-1
- Initial build


