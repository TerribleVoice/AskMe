import { useLayoutEffect } from "react";
import { FeedAuthorsSlider } from "./components/FeedAuthorsSlider";
import { FeedPosts } from "./components/FeedPosts";

export const FeedPage: React.FC = () => {
  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return (
    <>
    <div className={`feed_page`}>
      <FeedAuthorsSlider />
      <FeedPosts />
    </div>
    </>
  );
};
