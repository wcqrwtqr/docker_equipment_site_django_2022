from django.test import SimpleTestCase
from django.urls import resolve, reverse

from equipmentList.views import EquipmentCreateView, EquipmentDeleteView, EquipmentDetailView, EquipmentListView, EquipmentUpdateView
from equipmenMaintenance.views import MaintenanceCreate, MaintenanceDeleteView, MaintenanceDetailView, MaintenanceUpdateView, MaintenanceHomePage
from jobs.views import JobsCreate, JobsDeleteView, JobsDetailView, JobsUpdateView, JobsHomePage
from dailyreport.views import DailyReportListView, DailyreportCreate, DailyreportUpdateView, DailyreportDeleteView, DailyreportDetailView
from dashboard.views import DashHomePage, DashboardQueryOne, DashboardQueryMain, DashboardQueryDailyreport, DashboardQueryJobs

class TestUrls(SimpleTestCase):

    def test_equipmentlistview_url_resolves(self):
        url = reverse('equipment')
        self.assertURLEqual(resolve(url).func.view_class, EquipmentListView)

    def test_equipmentdetails_url_resolves(self):
        url = reverse('equipment_detail', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, EquipmentDetailView)

    def test_equipmentcreate_url_resolves(self):
        url = reverse('equipment_new')
        self.assertURLEqual(resolve(url).func.view_class, EquipmentCreateView)

    def test_equipmentdelete_url_resolves(self):
        url = reverse('equipment_delete',args=[1])
        self.assertURLEqual(resolve(url).func.view_class, EquipmentDeleteView)

    def test_equipmentupdate_url_resolves(self):
        url = reverse('equipment_update',args=[1])
        self.assertURLEqual(resolve(url).func.view_class, EquipmentUpdateView)

    def test_maintenancehome_url_resolves(self):
        url = reverse('maintenance')
        self.assertURLEqual(resolve(url).func.view_class, MaintenanceHomePage)

    def test_maintenancedetails_url_resolves(self):
        url = reverse('maintenance_detail', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, MaintenanceDetailView)

    def test_maintenancedelete_url_resolves(self):
        url = reverse('maintenance_delete', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, MaintenanceDeleteView)

    def test_maintenancecreate_url_resolves(self):
        url = reverse('maintenance_new')
        self.assertURLEqual(resolve(url).func.view_class, MaintenanceCreate)

    def test_maintenanceupdate_url_resolves(self):
        url = reverse('maintenance_update', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, MaintenanceUpdateView)

    def test_jobhome_url_resolves(self):
        url = reverse('jobs')
        self.assertURLEqual(resolve(url).func.view_class, JobsHomePage)

    def test_jobcreate_url_resolves(self):
        url = reverse('jobs_new')
        self.assertURLEqual(resolve(url).func.view_class, JobsCreate)

    def test_jobdelete_url_resolves(self):
        url = reverse('jobs_delete', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, JobsDeleteView)

    def test_jobdetail_url_resolves(self):
        url = reverse('jobs_detail', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, JobsDetailView)

    def test_jobupdate_url_resolves(self):
        url = reverse('jobs_update', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, JobsUpdateView)

    def test_dailyhome_url_resolves(self):
        url = reverse('dailyreport')
        self.assertURLEqual(resolve(url).func.view_class, DailyReportListView)

    def test_dailydetail_url_resolves(self):
        url = reverse('dailyreport_detail', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, DailyreportDetailView)

    def test_dailydelete_url_resolves(self):
        url = reverse('dailyreport_delete', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, DailyreportDeleteView)

    def test_dailyupdate_url_resolves(self):
        url = reverse('dailyreport_update', args=[1])
        self.assertURLEqual(resolve(url).func.view_class, DailyreportUpdateView)

    def test_dailycreate_url_resolves(self):
        url = reverse('dailyreport_new')
        self.assertURLEqual(resolve(url).func.view_class, DailyreportCreate)

    def test_dashboardhome_url_resolves(self):
        url = reverse('dashboard')
        self.assertURLEqual(resolve(url).func.view_class, DashHomePage)

    def test_dashboardone_url_resolves(self):
        url = reverse('dashboardQuery')
        self.assertURLEqual(resolve(url).func.view_class, DashboardQueryOne)

    def test_dashboardmaintenance_url_resolves(self):
        url = reverse('dashboardQueryMain')
        self.assertURLEqual(resolve(url).func.view_class, DashboardQueryMain)

    def test_dashboardjobs_url_resolves(self):
        url = reverse('dashboardQueryJobs')
        self.assertURLEqual(resolve(url).func.view_class, DashboardQueryJobs)

    def test_dashboarddailyreport_url_resolves(self):
        url = reverse('dashboardQueryDaily')
        self.assertURLEqual(resolve(url).func.view_class, DashboardQueryDailyreport)
