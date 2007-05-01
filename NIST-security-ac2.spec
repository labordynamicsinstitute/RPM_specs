Summary:  Implements AC-02 (NIST 800-53)
Name: NIST-security-ac2
Version: 1.0
Release: 0
License: GPL
Vendor: Mohammed Chaudhry
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Group: System/Security
Source0: dormant.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
%define filename    %{name}.sh

%description
This implements control AC-02 Account Management (NIST 800-53): 
"The organization manages information system accounts, including
establishing, activating, modifying, reviewing, disabling, and removing
accounts. The organization reviews information system accounts on a monthly
basis. The organization employs automated mechanisms to support the
management of information system accounts. The information system
automatically terminates temporary and emergency accounts after 30
days. The information system automatically disables inactive accounts after
45 days." It verifies accounts for the last time logged in, not using 'lastlog' 
because unreliable in the presence of NX logins.

%prep
%setup -n dormant

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755  %buildroot/var/log/
install -d -m 700  %buildroot/var/log/dormant
install -d -m 755  %buildroot/etc/cron.daily
install -d -m 755  %buildroot/etc/profile.d
install dormant.pl %buildroot/var/log/dormant/
touch  %buildroot/var/log/dormant/exclude
touch  %buildroot/var/log/dormant/userList
touch  %buildroot/var/log/dormant/userlogins
install lock_dormant_accounts %buildroot/etc/cron.daily/
install dormant_accounts.sh %buildroot/etc/profile.d/

%clean
#rm -rf $RPM_BUILD_ROOT


%files
%defattr(600,root,root,-)
%attr(700,root,root) /var/log/dormant/dormant.pl
%attr(700,root,root) /etc/cron.daily/lock_dormant_accounts
%attr(644,root,root) /etc/profile.d/dormant_accounts.sh
%attr(602,root,root) /var/log/dormant/userlogins
%config /var/log/dormant/userList
%config /var/log/dormant/exclude

%changelog
* Tue May  1 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1.0-0
- Initial build.

