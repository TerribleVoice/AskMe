import { UserSettings } from "@/pages/user_settings_page/components/UserSettings/UserSettings";
import { UserSettingsForm } from "./components/UserSettings/UserSettingsForm";
import { UserSettingsSubscriptions } from "./components/UserSettings/UserSettingsSubscriptions";

export const UserSettingsPage = () => {
  return (
    <>
      <UserSettingsForm />
      <UserSettingsSubscriptions />
    </>
  );
};
