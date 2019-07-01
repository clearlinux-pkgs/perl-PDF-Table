#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Table
Version  : 0.11.0
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-0.11.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-0.11.0.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-table-perl/libpdf-table-perl_0.10.1-1.debian.tar.xz
Summary  : Perl/CPAN Module PDF::Table: A utility class for building table layouts in a PDF::API2 object.
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PDF-Table-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description


%package dev
Summary: dev components for the perl-PDF-Table package.
Group: Development
Provides: perl-PDF-Table-devel = %{version}-%{release}
Requires: perl-PDF-Table = %{version}-%{release}
Requires: perl-PDF-Table = %{version}-%{release}

%description dev
dev components for the perl-PDF-Table package.


%package license
Summary: license components for the perl-PDF-Table package.
Group: Default

%description license
license components for the perl-PDF-Table package.


%prep
%setup -q -n PDF-Table-0.11.0
cd ..
%setup -q -T -D -n PDF-Table-0.11.0 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/PDF-Table-0.11.0/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PDF-Table
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-PDF-Table/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/PDF/Table.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::Table.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PDF-Table/deblicense_copyright
