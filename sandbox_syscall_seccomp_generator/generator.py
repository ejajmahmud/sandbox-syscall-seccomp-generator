"""Core Sandbox Syscall Seccomp Generator implementation."""
import json
from typing import Dict, List, Any, Optional


class SandboxSyscallSeccompGenerator:
    BASE_SAFE_SYSCALLS = [
        "read", "write", "openat", "close", "fstat", "lseek", "mmap", "mprotect",
        "munmap", "brk", "rt_sigaction", "rt_sigprocmask", "rt_sigreturn", "ioctl",
        "access", "pipe2", "select", "sched_yield", "getpid", "exit_group", "futex"
    ]

    NETWORK_SYSCALLS = [
        "socket", "connect", "sendto", "recvfrom", "getsockname", "getpeername"
    ]

    def __init__(self):
        pass

    def generate_profile(self, allow_network: bool = False, extra_syscalls: Optional[List[str]] = None) -> Dict[str, Any]:
        allowed = list(self.BASE_SAFE_SYSCALLS)
        if allow_network:
            allowed.extend(self.NETWORK_SYSCALLS)
        if extra_syscalls:
            allowed.extend(extra_syscalls)

        profile = {
            "defaultAction": "SCMP_ACT_ERRNO",
            "architectures": [
                "SCMP_ARCH_X86_64",
                "SCMP_ARCH_AARCH64"
            ],
            "syscalls": [
                {
                    "names": sorted(list(set(allowed))),
                    "action": "SCMP_ACT_ALLOW"
                }
            ]
        }
        return profile
