let
  pkgs = import <nixpkgs> {};
  pythonPackages = pkgs.python3Packages;
in pythonPackages.buildPythonPackage rec {
  name = "mailserver";
  src = ./.;
  propagatedBuildInputs = [
    pythonPackages.salmon-mail
  ];
}

