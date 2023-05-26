import { FeedAuthorsSlider } from "./components/FeedAuthorsSlider";
import { FeedPosts } from "./components/FeedPosts";

export const FeedPage: React.FC = () => {
  return (
    <>
      <FeedAuthorsSlider />
      <FeedPosts />
    </>
  );
};
