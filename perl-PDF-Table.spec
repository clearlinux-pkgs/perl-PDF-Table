#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Table
Version  : 1.002
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-1.002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OM/OMEGA/PDF-Table-1.002.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-table-perl/libpdf-table-perl_0.10.1-1.debian.tar.xz
Summary  : 'A utility class for building table layouts in a PDF::Builder  (or PDF::API2) object.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PDF-Table-license = %{version}-%{release}
Requires: perl-PDF-Table-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description


%package dev
Summary: dev components for the perl-PDF-Table package.
Group: Development
Provides: perl-PDF-Table-devel = %{version}-%{release}
Requires: perl-PDF-Table = %{version}-%{release}

%description dev
dev components for the perl-PDF-Table package.


%package license
Summary: license components for the perl-PDF-Table package.
Group: Default

%description license
license components for the perl-PDF-Table package.


%package perl
Summary: perl components for the perl-PDF-Table package.
Group: Default
Requires: perl-PDF-Table = %{version}-%{release}

%description perl
perl components for the perl-PDF-Table package.


%prep
%setup -q -n PDF-Table-1.002
cd %{_builddir}
tar xf %{_sourcedir}/libpdf-table-perl_0.10.1-1.debian.tar.xz
cd %{_builddir}/PDF-Table-1.002
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PDF-Table-1.002/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PDF-Table
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-PDF-Table/52fe44c5a3cfc7ed3d8d3018260f1d76828c9351
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::Table.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PDF-Table/52fe44c5a3cfc7ed3d8d3018260f1d76828c9351

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/PDF/Table.pm
