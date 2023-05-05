import { graphql } from "gatsby";

export const query = graphql`
  fragment F${NAME} on Sanity${NAME} {
    title
    cta {
      ...FCta
    }
    resume {
      ...FResume
    }
    photo {
      ...FPhoto
    }
  }
`;
