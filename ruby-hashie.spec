#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	hashie
Summary:	Your friendly neighborhood hash toolkit
Name:		ruby-%{pkgname}
Version:	5.1.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	8cf083973e76dbd103df554b062cf036
URL:		https://github.com/intridea/hashie
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-growl
BuildRequires:	ruby-guard
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake < 0.10
BuildRequires:	ruby-rake >= 0.9.2
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hashie is a small collection of tools that make hashes more powerful.
Currently includes Mash (Mocking Hash) and Dash (Discrete Hash).

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md CONTRIBUTING.md LICENSE UPGRADING.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
