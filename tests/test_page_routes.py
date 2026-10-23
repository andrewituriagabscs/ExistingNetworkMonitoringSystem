import unittest

import app


class PageRoutesTest(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()

    def test_navigation_routes_return_200(self):
        paths = [
            "/",
            "/dashboard",
            "/Dashboard",
            "/monitor",
            "/Monitor",
            "/alerts",
            "/Alerts",
            "/reports",
            "/Reports",
            "/ping-records",
            "/Ping-Records",
            "/ml-insights",
            "/ML-Insights",
            "/settings",
            "/Settings",
            "/about",
            "/About",
        ]
        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)

    def test_navigation_html_contains_links_and_history_routing(self):
        response = self.client.get("/alerts")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)

        # Check navigation anchor links
        self.assertIn('href="/dashboard"', html)
        self.assertIn('href="/monitor"', html)
        self.assertIn('href="/alerts"', html)
        self.assertIn('href="/reports"', html)
        self.assertIn('href="/ml-insights"', html)
        self.assertIn('href="/settings"', html)
        self.assertIn('href="/about"', html)

        # Check client-side seamless URL history logic
        self.assertIn("switchView(viewName", html)
        self.assertIn("history.pushState({ view: viewName }", html)
        self.assertIn("window.addEventListener('popstate'", html)
        self.assertIn("const urlViewMap =", html)


if __name__ == "__main__":
    unittest.main()
