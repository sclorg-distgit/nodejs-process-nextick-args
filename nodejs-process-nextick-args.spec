# spec file for package nodejs-nodejs-process-nextick-args
%{?scl:%scl_package nodejs-nodejs-process-nextick-args}
%{!?scl:%global pkg_name %{name}}

%global npm_name process-nextick-args
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-process-nextick-args
Version:    1.0.7
Release:    1%{?dist}
Summary:	process.nextTick but always with args
Url:		https://github.com/calvinmetcalf/process-nextick-args
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
process.nextTick but always with args

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test.js
%endif

%files
%{nodejs_sitelib}/process-nextick-args

%doc readme.md license.md

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.7-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-4
- Rebuilt with updated metapackage

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial build
