Name: jags
Version: 1.0.3
Release: 1%{?dist}
Summary: Just Another Gibbs Sampler
URL: http://mcmc-jags.sourceforge.net
Source0: http://mcmc-jags.sourceforge.net/JAGS-%{version}.tar.gz
License: GPLv2
Group: Applications/Engineering
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-gfortran, gcc-c++, lapack-devel, blas-devel

%description
JAGS (Just Another Gibbs Sampler) is a program for the analysis of
Bayesian statistical models using Markov Chain Monte Carlo (MCMC)
simulation.

JAGS is similar to the BUGS (Bayesian Inference using Gibbs Sampling)
program developed at the MRC Biostatistics Unit, Cambridge, and uses a
dialect of the BUGS language to describe Bayesian hierarchical models.

%package devel
Summary: JAGS development libraries
Group: Applications/Engineering
Requires: jags  = %{version}
Requires: gcc-c++, gcc-gfortran
%description devel

JAGS headers and libraries. Install jags-devel if you are going to 
link a program against the JAGS library, or extend the functionality
of JAGS by developing/installing JAGS modules.

%prep 
%setup -q -n JAGS-%{version}

export F77=gfortran
%configure 
make 

%install
make install DESTDIR=${RPM_BUILD_ROOT} 

%files
%defattr(-, root, root)
%{_bindir}/jags
%{_libexecdir}/jags-terminal
%{_libdir}/JAGS
%{_libdir}/libjags.la
%{_libdir}/libjags.so.*
%{_libdir}/libjrmath.la
%{_libdir}/libjrmath.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/jags.pc
%{_includedir}/JAGS
%{_libdir}/libjags.so
%{_libdir}/libjrmath.so

%clean
rm -rf ${RPM_BUILD_ROOT};

%post 
/sbin/ldconfig

%postun 
/sbin/ldconfig

%changelog
* Thu Jul 17 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.3-1
- Built JAGS 1.0.3

* Tue May 20 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-3
- Modified descriptions
- Built on Fedora 9.

* Mon May 19 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-2
- Moved libjags.so and libjrmath.so into devel package
- Added blas-devel as build requirement

* Fri May 16 2008 Martyn Plummer <martyn_plummer@sourceforge.net> 1.0.2-1
- First attempt
