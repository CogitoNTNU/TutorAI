import axios from "axios";
import { describe, it, expect, vi } from "vitest";
import postLoginAttempt from "../../src/services/LoginService";

// Mock data
const mockTraversalMethods = {
  username: "test",
  password: "test",
};

// Create a mock for axios.post
vi.spyOn(axios, "post").mockResolvedValue({
  status: 200,
  data: mockTraversalMethods,
});

describe("LoginService Service when logging into valid account", () => {
  it("Should return a user", async () => {
    const user = await postLoginAttempt(
      mockTraversalMethods.username,
      mockTraversalMethods.password
    );

    expect(user).toEqual(mockTraversalMethods);
  });
});
