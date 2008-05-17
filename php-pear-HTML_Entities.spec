%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Entities
%define		_status		alpha
%define		_pearname	HTML_Entities
Summary:	%{_pearname} - konvert text to/from HTML entities
Summary(pl.UTF-8):	%{_pearname} - konwersja tekstu do/z encji HTML
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5e8db2985d5e9ffd72894761f062c21a
URL:		http://pear.php.net/package/HTML_Entities/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to convert utf-8 text to html entities and
vice-versa. It provides functions similar to php functions
html_entity_decode, htmlentities and get_html_translation_table, but
it works properly with utf-8 in PHP4, and contains ALL defined HTML
entities.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten pozwala na konwersję tekstu utf-8 do/z encji html. Pakiet
dostarcza funkcjonalność zbliżoną do funkcji PHP takich jak
html_entity_decode, htmlentities i get_html_translation_table, jednak
działa poprawnie z utf-8 w PHP 4 oraz zawiera wszystkie zdefiniowane
encje HTML.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/HTML_Entities/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/Entities
%{php_pear_dir}/HTML/Entities.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_Entities
