#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Scope-Upper
Version  : 0.32
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/V/VP/VPIT/Scope-Upper-0.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VP/VPIT/Scope-Upper-0.32.tar.gz
Summary  : Act on upper scopes.
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Scope-Upper-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Scope::Upper - Act on upper scopes.
VERSION
Version 0.32
SYNOPSIS
"reap", "localize", "localize_elem", "localize_delete" and "WORDS" :

%package dev
Summary: dev components for the perl-Scope-Upper package.
Group: Development
Requires: perl-Scope-Upper-lib = %{version}-%{release}
Provides: perl-Scope-Upper-devel = %{version}-%{release}
Requires: perl-Scope-Upper = %{version}-%{release}
Requires: perl-Scope-Upper = %{version}-%{release}

%description dev
dev components for the perl-Scope-Upper package.


%package lib
Summary: lib components for the perl-Scope-Upper package.
Group: Libraries

%description lib
lib components for the perl-Scope-Upper package.


%prep
%setup -q -n Scope-Upper-0.32

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Scope/Upper.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Scope::Upper.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Scope/Upper/Upper.so
