# -*- coding: utf-8 -*-

import os
from datetime import datetime

from radish.config import Config
from radish.filesystemhelper import FileSystemHelper as fsh
from radish.exceptions import RadishError


class XunitWriter(object):
    REPORT_FILENAME = "radishtests.xml"
    ONE_XUNIT = "radish.one_xunit"

    def __init__(self, endResult):
        self._endResult = endResult

    def generate(self):
        try:
            from lxml import etree
        except:
            raise RadishError("No lxml support. Please install python-lxml")

        outputs = {}
        if Config().split_xunit:
            for f in self._endResult.get_features():
                filename = fsh.filename(f.get_filename(), with_extension=False)
                path = os.path.join(Config().xunit_file, filename + ".xml")
                if path not in outputs:
                    outputs[path] = []
                outputs[path].append(f)
        else:
            outputs[XunitWriter.ONE_XUNIT] = self._endResult.get_features()

        for filename, features in outputs.iteritems():
            if filename == XunitWriter.ONE_XUNIT:
                filename = Config().xunit_file or XunitWriter.REPORT_FILENAME

            testsuites = etree.Element("testsuites")

            for f in features:
                testsuite = etree.Element(
                    "testsuite",
                    name="radish",
                    hostname="localhost",
                    id=unicode(Config().marker),
                    time=str(f.get_duration()),
                    tests=str(sum([len(s.get_steps()) for s in f.get_scenarios()])),
                    failures=str(sum([sum([step.has_passed() is False for step in s.get_steps()]) for s in f.get_scenarios()])),
                    skipped=str(sum([sum([step.has_passed() is None for step in s.get_steps()]) for s in f.get_scenarios()])),
                    errors="0",
                    timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                )

                # append feature description to testsuite
                description = etree.Element(
                    "description",
                )
                description.text = etree.CDATA(f.get_description())
                testsuite.append(description)

                # append steps to testsuite
                for s in f.get_scenarios():
                    for step in s.get_steps():
                        testsuite.append(step.get_report_as_xunit_tag())

                testsuites.append(testsuite)

            with open(filename, "w") as f:
                f.write(etree.tostring(testsuites, pretty_print=True, xml_declaration=True, encoding="utf-8"))
