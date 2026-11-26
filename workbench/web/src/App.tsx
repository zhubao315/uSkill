import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import { Layout } from './components/Layout';
import { AgentsPage } from './pages/AgentsPage';
import { DashboardPage } from './pages/DashboardPage';
import { RunsPage } from './pages/RunsPage';
import { SkillDetailPage } from './pages/SkillDetailPage';
import { SkillsPage } from './pages/SkillsPage';

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<DashboardPage />} />
          <Route path="skills" element={<SkillsPage />} />
          <Route path="skills/:skillId" element={<SkillDetailPage />} />
          <Route path="agents" element={<AgentsPage />} />
          <Route path="runs" element={<RunsPage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
