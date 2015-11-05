BuildRequires: gcc-fortran
Name: aml
License: Commercial
Group: Application/Statistics
Summary: aML is a statistical software package for estimating multilevel, multiprocess models.
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.09
Release: 3
Source0: aml-%{version}-lv-3.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64 i386 x86_64
URL: http://www.applied-ml.com

%description
aML is a statistical software package for estimating multilevel, multiprocess models. Multilevel refers to the capability of handling repeated measures of outcomes; the number of levels may be arbitrarily large. Multiprocess refers to the capability of jointly estimating several outcome types, with residuals that may be correlated across outcome types. It handles a wide variety of models to support continuous outcomes, ordered and unordered categorical outcomes, duration (hazard) outcomes, and count outcomes. Many generalizations are supported, such as selection models, random coefficients models, growth models, ordered probit/logit models, sequential probit/logit models, multinomial probit/logit models, Tobit models, et cetera. All may have arbitrarily many levels and all may be mixed and matched as desired. Included with aML are a data preprocessing program and several utilities to make life easier.
More information at http://www.applied-ml.com/product/index.html
%prep
%setup 

%build
cd Lib
make
cd ../aML
cp ../Source/makefile .
make
cd ../Peripherals
make
cd ../Raw2aml
make

%install
install -d -m 755 -g root -o root %buildroot/usr/local/bin
install -m 0755 -o root -g users aML/aml %buildroot/usr/local/bin/aml
install -m 0755 -o root -g users aML/bigaml %buildroot/usr/local/bin/bigaml
install -m 0755 -o root -g users aML/hugeaml %buildroot/usr/local/bin/hugeaml
install -m 0755 -o root -g users Raw2aml/raw2aml %buildroot/usr/local/bin/raw2aml
install -m 0755 -o root -g users Peripherals/amltest %buildroot/usr/local/bin/amltest
install -m 0755 -o root -g users Peripherals/mktab %buildroot/usr/local/bin/mktab
install -m 0755 -o root -g users Peripherals/points %buildroot/usr/local/bin/points
install -m 0755 -o root -g users Peripherals/update %buildroot/usr/local/bin/update

%clean

%files
%doc readme.txt
/usr/local/bin/aml
/usr/local/bin/bigaml
/usr/local/bin/hugeaml
/usr/local/bin/mktab
/usr/local/bin/amltest
/usr/local/bin/points
/usr/local/bin/update
/usr/local/bin/raw2aml


%changelog
* Tue Jul 17 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 2.09-2
- Modified to use gfortran instead of f77

* Mon Jan 30 2006 vilhuber@lservices
- First open-source version
* Fri Jan 13 2006 vilhuber@lservices
- Initial RPM
