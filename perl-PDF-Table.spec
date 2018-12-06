#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Table
Version  : 0.10.1
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-0.10.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-0.10.1.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-table-perl/libpdf-table-perl_0.10.1-1.debian.tar.xz
Summary  : 'A utility class for building table layouts in a PDF::API2 object.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description


%package dev
Summary: dev components for the perl-PDF-Table package.
Group: Development
Provides: perl-PDF-Table-devel = %{version}-%{release}

%description dev
dev components for the perl-PDF-Table package.


%prep
%setup -q -n PDF-Table-0.10.1
cd ..
%setup -q -T -D -n PDF-Table-0.10.1 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/PDF-Table-0.10.1/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.1PDF/Table.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::Table.3
