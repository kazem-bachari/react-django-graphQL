import { gql, useQuery } from "@apollo/client";
import { useEffect } from "react";
import { loadErrorMessages, loadDevMessages } from "@apollo/client/dev";
const QUERY = gql`
  {
    books {
      title
      description
      category {
        title
      }
    }
    categorizes {
      title
    }
  }
`;
type book = {
  id: number;
  title: string;
  description: string;
  category: { title: string };
};
type category = {
  title: string;
};
function App() {
  loadDevMessages();
  loadErrorMessages();
  // @ts-ignore
  const { data, loading, error } = useQuery(QUERY);
  useEffect(() => {
    console.log(data);
  });
  if (error) return <pre>{error.message}</pre>;
  else if (loading) return <h1>Loading ....</h1>;
  else
    return (
      <>
        <div className="App">
          {data.books.map((book: book) => (
            <div>
              <h3>{book.title}</h3>
              <p>{book.description}</p>
              <span>{book.category.title}</span>
              <hr />
            </div>
          ))}
        </div>
        <div>
          {data.categorizes.map((category: category) => (
            <h1>{category.title}</h1>
          ))}
        </div>
      </>
    );
}

export default App;
