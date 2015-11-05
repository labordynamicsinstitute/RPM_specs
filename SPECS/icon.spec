Summary: Icon is a high-level, general-purpose programming language with a large repertoire of features for processing data structures and character strings. Icon is an imperative, procedural language with a syntax reminiscent of C and Pascal, but with semantics at a much higher level.
Name: icon
Version: 9.4.3
Release: 1
License: Public Domain
Prefix: /usr/local
Group: Languages
URL: http://www.cs.arizona.edu/icon/index.htm
Source0: icon.v943src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel gcc
%description

%prep
%setup -q -n icon.v943src

%build
set
make X-Configure name=linux
make
make Test

%install
install -d -m 755 %buildroot/usr/local/bin
install -d -m 755 %buildroot/usr/local/icon/bin
install -d -m 755 %buildroot/usr/local/icon/lib
install    -m 755 bin/* %{buildroot}/usr/local/icon/bin  
install    -m 755 lib/* %{buildroot}/usr/local/icon/lib  
# man pages
install -d -m 755 %buildroot/usr/local/share/man/man1
install    -m 755 man/man1/icon*.1 %buildroot/usr/local/share/man/man1
# link in the binaries
cd %{buildroot}/usr/local/bin/
ln -s ../icon/bin/icon .
ln -s ../icon/bin/icont .
ln -s ../icon/bin/iconx .
ln -s ../icon/bin/vib .

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/
/usr/local/share/man/man1/icon.1
/usr/local/share/man/man1/icont.1
/usr/local/icon
/usr/local/bin/icon
/usr/local/bin/icont
/usr/local/bin/iconx
/usr/local/bin/vib

%changelog
* Tue Apr 25 2006 Lars Vilhuber <lars.vilhuber@cornell.edu> - 
- Initial build.


