Summary: Documentation on tools to configure a VirtualRDC 
Name: virtualrdc_sashelp
Version: 1.0.1
Release: 1
Copyright: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch


%description
* Provides documentatation on how to configure the VirtualRDC

%requires: 
%prep 
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
mkdir -p $MYBUILD

%build
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
rsync --delete -a %_topdir/../documentation/SAS/ $MYBUILD/

%install
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
rm -rf $RPM_BUILD_ROOT/
install -d -m 755 $RPM_BUILD_ROOT/usr/local/share/doc/SAS
cp -a $MYBUILD/* $RPM_BUILD_ROOT/usr/local/share/doc/SAS
chmod -R a+rX $RPM_BUILD_ROOT/usr/local/share/doc/SAS

%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(-,root,root) 
/usr/local/share/doc/SAS/ODS/ODS-notes.seminar.txt
/usr/local/share/doc/SAS/ODS/index.html
/usr/local/share/doc/SAS/ODS/ODS-notes.class.txt
/usr/local/share/doc/SAS/index.html
/usr/local/share/doc/SAS/Efficiencies/ReadMe.txt
/usr/local/share/doc/SAS/Efficiencies/SAS_Efficiencies.txt
/usr/local/share/doc/SAS/Efficiencies/SAS_notes.PDF
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/procappend.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/sqlindex.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/datamerge.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/example-frame2.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/Double_set.zip
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchindex.ksh
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.lst.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-sqlnokey.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/index.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchmark.ksh
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/datainterleave.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/example-frame.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/example.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.log.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchmark.0.1.ksh
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchmark.0.2.ksh
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/NOTES.TXT
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/results.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/mergeindex.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchcreate.ksh
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-indexset2.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-indexset3.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-indexset4.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/example-main.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/benchmark.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.lst
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-key.sas
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/sqlnoind.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/setkey.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/autoexec.sas
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/createindex.html
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-mergesort2.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-mergesort3.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-mergesort4.log
/usr/local/share/doc/SAS/Efficiencies/LarsKevin/test-sqlset.log
/usr/local/share/doc/SAS/Efficiencies/index.html
/usr/local/share/doc/SAS/Efficiencies/OW_apro.exe

%changelog
* Mon Feb 21 2005 vilhuber
  - first version. Based on /data/doc/Coursework/SAS

