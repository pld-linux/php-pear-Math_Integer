%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Integer
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Package to represent and manipulate integers
Summary(pl):	%{_class}_%{_subclass} - pakiet do reprezentacji i obliczeñ na liczbach ca³kowitych
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	54a64c880e7d4910280a475871798279
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class Math_Integer can represent integers bigger than the signed
longs that are the default of PHP, if either the GMP or the BCMATH
(bundled with PHP) are present. Otherwise it will fall back to the
internal integer representation. The Math_IntegerOp class defines
operations on Math_Integer objects.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa Math_Integer mo¿e reprezentowaæ liczby ca³kowite wiêksze ni¿
long ze znakiem, który jest domy¶lnym typem w PHP - o ile obecne jest
jedno z rozszerzeñ GMP i BCMATH (do³±czanych do dystrybucji PHP). W
przeciwnym wypadku klasa u¿yje wewnêtrznej reprezentacji liczb
ca³kowitych. Klasa Math_IntegerOp definiuje operacje na obiektach
klasy Math_Integer.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test/*
%{php_pear_dir}/%{_class}/*.php
