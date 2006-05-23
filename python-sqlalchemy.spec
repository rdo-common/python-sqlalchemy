%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}


%define srcname SQLAlchemy

Name:           python-sqlalchemy
Version:        0.1.7
Release:        1%{?dist}
Summary:        Modular and flexible ORM library for python

Group:          Development/Libraries
License:        MIT
URL:            http://www.sqlalchemy.org/
Source0:        http://download.sourceforge.net/sqlalchemy/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python python-setuptools
Requires:       python-abi = %{pyver}

%description
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --single-version-externally-managed
# remove unnecessary scripts for building documentation
rm -rf doc/build

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE PKG-INFO doc examples
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info
%dir %{python_sitelib}/sqlalchemy
%{python_sitelib}/sqlalchemy/*.py
%{python_sitelib}/sqlalchemy/*.pyc
%ghost %{python_sitelib}/sqlalchemy/*.pyo
%dir %{python_sitelib}/sqlalchemy/databases
%{python_sitelib}/sqlalchemy/databases/*.py
%{python_sitelib}/sqlalchemy/databases/*.pyc
%ghost %{python_sitelib}/sqlalchemy/databases/*.pyo
%dir %{python_sitelib}/sqlalchemy/ext
%{python_sitelib}/sqlalchemy/ext/*.py
%{python_sitelib}/sqlalchemy/ext/*.pyc
%ghost %{python_sitelib}/sqlalchemy/ext/*.pyo
%dir %{python_sitelib}/sqlalchemy/mapping
%{python_sitelib}/sqlalchemy/mapping/*.py
%{python_sitelib}/sqlalchemy/mapping/*.pyc
%ghost %{python_sitelib}/sqlalchemy/mapping/*.pyo
%dir %{python_sitelib}/sqlalchemy/mods
%{python_sitelib}/sqlalchemy/mods/*.py
%{python_sitelib}/sqlalchemy/mods/*.pyc
%ghost %{python_sitelib}/sqlalchemy/mods/*.pyo

%changelog
* Tue May 16 2006 Shahms E. King <shahms@shahms.com> 0.1.7-1
- Update to new upstream version
- Point URL to direct link, not sourceforge redirect
- Remove unnecessary document build scripts

* Fri Apr 14 2006 Shahms E. King <shahms@shahms.com> 0.1.6-1
- Initial package
