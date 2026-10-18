import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from powerbi_support import valid_embed_url
from streamlit.testing.v1 import AppTest
ROOT=Path(__file__).resolve().parents[1]

class ResearchAppTests(unittest.TestCase):
    def test_embed_origin(self):
        self.assertTrue(valid_embed_url('https://app.powerbi.com/view?r=example'))
        self.assertTrue(valid_embed_url('https://app.powerbi.com/reportEmbed?reportId=example'))
        for url in ['https://evil.test/view?r=x','https://app.powerbi.com.evil.test/view?r=x','http://app.powerbi.com/view?r=x','https://app.powerbi.com@evil.test/view?r=x','https://teams.cloud.microsoft/','https://app.powerbi.com/view']:
            self.assertFalse(valid_embed_url(url))
    def test_dashboard_views(self):
        at=AppTest.from_file(str(ROOT/'app.py'),default_timeout=40).run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.tabs),7)
        for view in ['HIV vs ART coverage','GDP growth comparison','Country indicator lookup']:
            at.radio[0].set_value(view).run()
            self.assertFalse(at.exception, str(at.exception))
        at.slider[0].set_value((1990,1990)).run()
        self.assertFalse(at.exception)
        at.multiselect[0].set_value([]).run()
        self.assertFalse(at.exception)
if __name__=='__main__': unittest.main()
