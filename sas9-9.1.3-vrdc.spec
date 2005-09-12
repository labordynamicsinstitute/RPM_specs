Name: sas9
License: Commercial
Group: Application/Statistics
Summary: SAS 9.1.3 
Packager: Andrey Balyakin <aab24@cornell.edu>
Version: 9.1.3
Release: 1 
#Source0: 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch 

%description
Creates links for the SAS call chain 

%prep

%build

%install

%post

ln -s /opt/SAS_9.1.3_OR/sas /usr/local/bin/sas913
ln -s /usr/local/bin/sas913 /usr/local/bin/sas91
ln -s /usr/local/bin/sas91 /usr/local/bin/sas9
#ln -s /usr/local/bin/sas9 /usr/local/bin/sas

%preun

#rm /usr/local/bin/sas
rm /usr/local/bin/sas9
rm /usr/local/bin/sas91
rm /usr/local/bin/sas913

%postun

%clean

%files

%changelog
* Fri Jul 08 2005 Andrey Balyakin <aab24@cornell.edu>
- sas9 -> sas91 -> sas913 -> /opt/SAS_9.1.3_OR/sas call chain is created in /usr/local/bin 
