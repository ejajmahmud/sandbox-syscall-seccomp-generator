"""CLI for sandbox-syscall-seccomp-generator."""
import sys
import argparse
import json
from .generator import SandboxSyscallSeccompGenerator


def main():
    parser = argparse.ArgumentParser(description="Sandbox Syscall Seccomp Generator CLI")
    parser.add_argument("--demo", action="store_true", help="Run seccomp generator demo")
    args = parser.parse_args()

    if args.demo:
        gen = SandboxSyscallSeccompGenerator()
        profile = gen.generate_profile(allow_network=False)
        print("[+] Generated Hardened Seccomp Profile (JSON):")
        print(json.dumps(profile, indent=2))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
