Name: aml
License: Commercial
Group: Application/Statistics
Summary: aML is a statistical software package for estimating multilevel, multiprocess models.
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.80
Release: 0
Source0: aml.ia64.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64

%description
aML is a statistical software package for estimating multilevel, multiprocess models. Multilevel refers to the capability of handling repeated measures of outcomes; the number of levels may be arbitrarily large. Multiprocess refers to the capability of jointly estimating several outcome types, with residuals that may be correlated across outcome types. It handles a wide variety of models to support continuous outcomes, ordered and unordered categorical outcomes, duration (hazard) outcomes, and count outcomes. Many generalizations are supported, such as selection models, random coefficients models, growth models, ordered probit/logit models, sequential probit/logit models, multinomial probit/logit models, Tobit models, et cetera. All may have arbitrarily many levels and all may be mixed and matched as desired. Included with aML are a data preprocessing program and several utilities to make life easier.
More information at http://www.applied-ml.com/product/index.html
%prep

%build

%install
install -d -m 755 -g root -o root %buildroot/usr/local/bin
cd %buildroot/usr/local/bin
tar xzf %{SOURCE0}
chmod 0755 %buildroot/usr/local/bin/aml
chmod 0755 %buildroot/usr/local/bin/amltest
chmod 0755 %buildroot/usr/local/bin/bigaml
chmod 0755 %buildroot/usr/local/bin/borndate
chmod 0755 %buildroot/usr/local/bin/forprep
chmod 0755 %buildroot/usr/local/bin/hugeaml
chmod 0755 %buildroot/usr/local/bin/mktab
chmod 0755 %buildroot/usr/local/bin/points
chmod 0755 %buildroot/usr/local/bin/raw2aml
chmod 0755 %buildroot/usr/local/bin/update
chown root.root %buildroot/usr/local/bin/aml
chown root.root %buildroot/usr/local/bin/amltest
chown root.root %buildroot/usr/local/bin/bigaml
chown root.root %buildroot/usr/local/bin/borndate
chown root.root %buildroot/usr/local/bin/forprep
chown root.root %buildroot/usr/local/bin/hugeaml
chown root.root %buildroot/usr/local/bin/mktab
chown root.root %buildroot/usr/local/bin/points
chown root.root %buildroot/usr/local/bin/raw2aml
chown root.root %buildroot/usr/local/bin/update

%clean

%files
/usr/local/bin/aml
/usr/local/bin/amltest
/usr/local/bin/bigaml
/usr/local/bin/borndate
/usr/local/bin/forprep
/usr/local/bin/hugeaml
/usr/local/bin/mktab
/usr/local/bin/points
/usr/local/bin/raw2aml
/usr/local/bin/update


%changelog
* Fri Jan 13 2006 vilhuber@lservices
- Initial RPM
