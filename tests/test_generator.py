"""Unit tests for sandbox-syscall-seccomp-generator."""
import unittest
from sandbox_syscall_seccomp_generator.generator import SandboxSyscallSeccompGenerator


class TestSandboxSyscallSeccompGenerator(unittest.TestCase):
    def test_default_profile(self):
        g = SandboxSyscallSeccompGenerator()
        prof = g.generate_profile(allow_network=False)
        self.assertEqual(prof["defaultAction"], "SCMP_ACT_ERRNO")
        names = prof["syscalls"][0]["names"]
        self.assertIn("read", names)
        self.assertNotIn("socket", names)

    def test_network_inclusion(self):
        g = SandboxSyscallSeccompGenerator()
        prof = g.generate_profile(allow_network=True)
        names = prof["syscalls"][0]["names"]
        self.assertIn("socket", names)
