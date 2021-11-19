#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flit_core
Version  : 3.5.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/26/12/74c9b72b280006a97fb80268e6b84bf77c73837d93391c8238488c6f2dde/flit_core-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/26/12/74c9b72b280006a97fb80268e6b84bf77c73837d93391c8238488c6f2dde/flit_core-3.5.0.tar.gz
Summary  : Distribution-building parts of Flit. See flit package for more information
Group    : Development/Tools
License  : BSD-3-Clause
Requires: flit_core-python = %{version}-%{release}
Requires: flit_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the flit_core package.
Group: Default
Requires: flit_core-python3 = %{version}-%{release}

%description python
python components for the flit_core package.


%package python3
Summary: python3 components for the flit_core package.
Group: Default
Requires: python3-core
Provides: pypi(flit_core)
Requires: pypi(tomli)

%description python3
python3 components for the flit_core package.


%prep
%setup -q -n flit_core-3.5.0
cd %{_builddir}/flit_core-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637339141
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -m install --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
