from app.shell.command import Command


class ExperienceCommand(Command):

    name = "experience"

    aliases = [
        "exp"
    ]

    description = "Show professional experience"

    usage = "experience"


    help_text = """
experience

Displays professional work experience.

Usage:

experience
"""


    def execute(self, shell, args):

        return [

            "Professional Experience",

            "",

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",

            "PFH Technology (Nov. 2025 – Present)",
            "Warehouse Operative",
            "",
            "Configured, imaged, and deployed laptops, desktops, and peripherals to customer specifications, including OS installation and software builds.",
            "Maintained accurate IT asset inventory using ERP systems and barcode scanning to ensure stock accuracy and traceability.",
            "Prepared shipping documentation, updated warehouse records, and reconciled delivery manifests to support efficient logistics operations.",
            "Performed secure data wiping and supported IT asset lifecycle activities, including refurbishment and disposal, in compliance with data protection standards.",
            "Assisted in identifying and escalating hardware discrepancies while ensuring adherence to information security policies.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "Amazon (Oct. 2022 – Oct. 2025)",
            "Selling Partner Support Associate",
            "",
            "Delivered multi-channel support to Amazon Selling Partners, resolving account and platform-related enquiries with a strong customer focus.",
            "Investigated complex issues using analytical and problem-solving skills to provide accurate, policy-compliant solutions.",
            "Maintained strict compliance with Amazon's data security, confidentiality, and service level standards.",
            "Collaborated with internal teams to resolve escalated cases and improve the overall seller experience.",
            "Consistently provided high-quality support while meeting performance and productivity targets.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "HCL Technologies (Client: Nestlé) (Apr. 2022 – Aug. 2022)",
            "Critical Incident Management",
            "",
            "Coordinated critical IT incidents across North and Latin America, ensuring timely communication and resolution.",
            "Supported IT Crisis Management by facilitating incident response and problem management processes.",
            "Led Major Incident (P2) bridge calls, coordinating cross-functional teams and escalating issues where required.",
            "Performed quality assurance reviews of incident handling to improve service effectiveness and response times.",
            "Assisted support teams in correctly prioritising and categorising incidents to ensure appropriate escalation.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "Dell Technologies (May 2019 – Apr. 2022)",
            "Senior Support Analyst",
            "",
            "Delivered bilingual (Portuguese and English) technical support, diagnosing and resolving Windows, Microsoft 365, VPN, VMware, and enterprise software issues.",
            "Analysed system logs and Windows Registry entries to identify root causes and create technical documentation for the knowledge base.",
            "Managed Active Directory accounts, permissions, and disk quotas while collaborating with global support teams.",
            "Deployed and managed software using Microsoft SCCM and Workspace ONE, ensuring compliance with company standards.",
            "Maintained high standards of data integrity, customer privacy, and service delivery in a fast-paced enterprise environment.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "Plot – Visual Technologies (Nov. 2014 – Sep. 2017)",
            "Senior Support Technician",
            "",
            "Designed and implemented Audio-Visual solutions for Video Walls, SOC/NOC environments, digital signage, and conference rooms.",
            "Installed and configured servers, AV equipment, and supporting software to meet customer requirements.",
            "Developed backup and disaster recovery plans to support high availability and business continuity.",
            "Delivered technical support, preventative maintenance, and user training to ensure reliable system operation.",
            "Collaborated with clients to design cost-effective solutions, completing projects ahead of schedule through effective planning.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "Emater-RS/Ascar (Apr. 2014 – Nov. 2014)",
            "Support Analyst",
            "",
            "Installed and configured Windows operating systems and business applications across the organisation.",
            "Provided remote and on-site technical support via phone, email, and remote access tools.",
            "Diagnosed and resolved hardware and software issues while maintaining high customer service standards.",
            "Documented software defects with detailed reproduction steps, logs, and supporting evidence.",
            "Worked closely with development teams to facilitate timely issue resolution.",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "Netwall Tecnologia LTDA (Oct. 2011 – Sep. 2013)",
            "Support Analyst",
            "",
            "Installed, configured, and supported Linux-based software solutions for enterprise customers.",
            "Maintained internal IT infrastructure and provided on-site technical support.",
            "Diagnosed application issues remotely using SSH, log analysis, and Linux command-line tools.",
            "Documented software defects with detailed replication steps and technical evidence for development teams.",
            "Collaborated with developers to troubleshoot issues and improve software reliability."

        ]