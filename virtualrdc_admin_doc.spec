Summary: Documentation on tools to configure a VirtualRDC 
Name: virtualrdc_admin_doc
Version: 1.0.2
Release: 0
Copyright: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch


%description
* Provides documentatation on how to configure the VirtualRDC

%requires: acroread
%prep 
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
rm -rf $MYBUILD
mkdir -p $MYBUILD
cp -a %_topdir/../documentation/adminguide $MYBUILD/

%build
# we only build the latex part the rest is fine
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
cd $MYBUILD/adminguide
i=1
while [[ $i -le 3 ]]
do
  pdflatex "\nonstopmode\input{policy.administration.tex}"
  pdflatex "\nonstopmode\input{policy.user_guide.tex}"
  let i+=1
done

%install
export MYBUILD=$RPM_BUILD_DIR/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
rm -rf $RPM_BUILD_ROOT/
install -d -m 755 $RPM_BUILD_ROOT/usr/local/share/doc/virtualrdc
install -m 644    $MYBUILD/adminguide/policy.user_guide.pdf $RPM_BUILD_ROOT/usr/local/share/doc/virtualrdc/policy.user_guide.pdf
install -m 644    $MYBUILD/adminguide/policy.administration.pdf $RPM_BUILD_ROOT/usr/local/share/doc/virtualrdc/policy.administration.pdf


%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(-,root,root) 
/usr/local/share/doc/virtualrdc/policy.user_guide.pdf  
/usr/local/share/doc/virtualrdc/policy.administration.pdf


%changelog
* Sun Feb 20 2005 vilhuber
  - first version
