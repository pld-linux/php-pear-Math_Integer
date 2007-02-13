%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Integer
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_class}_%{_subclass} - Package to represent and manipulate integers
Summary(pl.UTF-8):	%{_class}_%{_subclass} - pakiet do reprezentacji i obliczeń na liczbach całkowitych
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	54a64c880e7d4910280a475871798279
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Math_Integer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class Math_Integer can represent integers bigger than the signed
longs that are the default of PHP, if either the GMP or the BCMATH
(bundled with PHP) are present. Otherwise it will fall back to the
internal integer representation. The Math_IntegerOp class defines
operations on Math_Integer objects.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Math_Integer może reprezentować liczby całkowite większe niż
long ze znakiem, który jest domyślnym typem w PHP - o ile obecne jest
jedno z rozszerzeń GMP i BCMATH (dołączanych do dystrybucji PHP). W
przeciwnym wypadku klasa użyje wewnętrznej reprezentacji liczb
całkowitych. Klasa Math_IntegerOp definiuje operacje na obiektach
klasy Math_Integer.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/test/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
